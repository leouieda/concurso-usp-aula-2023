"""
Use livereload to serve the content for local inspection.
"""
import sys
import subprocess
import logging
import shutil
from pathlib import Path
import livereload
import livereload.server


def build():
    """Rebuild the website."""
    subprocess.run(["jupyter-book", "build", "-q", "."])
    destination = Path("_build/html")
    sources = ["assets", "slides"]
    for source in sources:
        shutil.copytree(source, destination / source, dirs_exist_ok=True)


def patch_livereload(livereload):
    # Hack to make livereload work when serving MathJax locally.
    # See https://github.com/lepture/python-livereload/issues/174
    from pathlib import PosixPath
    from urllib.parse import urlparse
    # Tornado is a livereload dependency
    from tornado.web import OutputTransform

    # See https://github.com/GaretJax/sphinx-autobuild/issues/71#issuecomment-681854580
    class _FixedLiveScriptInjector(livereload.server.LiveScriptInjector):
        def __init__(self, request):
            # NOTE: Using super() here causes an infinite cycle, due to
            #       ConfiguredTransform not declaring an __init__.
            OutputTransform.__init__(self, request)

            # Determine if this is an HTML page
            path = PosixPath(urlparse(request.uri).path)
            self.should_modify_request = path.suffix in ["", ".html"]

        def transform_first_chunk(self, status_code, headers, chunk, finishing):
            if not self.should_modify_request:
                return status_code, headers, chunk
            return super().transform_first_chunk(status_code, headers, chunk, finishing)

    livereload.server.LiveScriptInjector = _FixedLiveScriptInjector


def serve():
    """Serve the website"""
    patch_livereload(livereload)
    livereload_logger = logging.getLogger("livereload")
    server = livereload.Server()

    home = Path(".")
    patterns = [
        "**/*.md",
        "**/*.ipynb",
        "**/index.html",
        "assets/*",
        "slides/*",
        "**/*.yml",
        "**/*.less",
        "**/*.css",
    ]
    watch = []
    for pattern in patterns:
        watch.extend(
            path for path in home.glob(pattern)
            if "_build" not in str(path.parent)
            and ".ipynb_checkpoints" not in str(path.parent)
            and path.name != "README.md"
        )
    print("Watching files:")
    for path in watch:
        print(f"  {path}")
        server.watch(str(path), build)

    port = 5500
    for attempt in range(10):
        try:
            server.serve(
                root=Path("_build") / "html",
                host="localhost",
                port=port,
                open_url_delay=1,
            )
            break
        except OSError:
            if attempt == max_attempts + 1:
                raise
            port += 1
            livereload_logger.handlers.clear()


if __name__ == "__main__":
    if "--serve" in sys.argv:
        build()
        serve()
    else:
        build()
