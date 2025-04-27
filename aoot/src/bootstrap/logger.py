import logging

from colorlog import ColoredFormatter


def setup_logger(*, is_test: bool = False):
    file_out = logging.FileHandler(
        "prod.log" if not is_test else "test.log", encoding="utf-8"
    )

    console_out = logging.StreamHandler()
    console_out.setFormatter(
        ColoredFormatter(
            "%(log_color)s%(name)s - %(levelname)s - %(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        )
    )

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
        handlers=(file_out, console_out),
    )
    logging.getLogger("asyncio").setLevel(logging.ERROR)
