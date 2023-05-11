import asyncio
import functools
from typing import Any, Callable, Dict, Optional, Type, Union

import typer
from typer.models import CommandFunctionType


class AsyncTyper(typer.Typer):
    """A subclass of Typer that allows for async functions to be used as commands.

    Usage:
        ```
        app = AsyncTyper()

        @app.async_command()
        async def my_async_command():
            ...


        @app.command()
        async def my_normal_command():
        ...
    """

    def async_command(
        self,
        name: Optional[str] = None,
        *,
        cls: Optional[Type] = None,
        context_settings: Optional[Dict[Any, Any]] = None,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
        short_help: Optional[str] = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        # Rich settings
        rich_help_panel: Union[str, None] = None,
    ) -> Callable[[CommandFunctionType], CommandFunctionType]:
        def decorator(async_func):
            @functools.wraps(async_func)
            def sync_func(*_args, **_kwargs):
                return asyncio.run(async_func(*_args, **_kwargs))

            self.command(
                name=name,
                cls=cls,
                context_settings=context_settings,
                help=help,
                epilog=epilog,
                short_help=short_help,
                options_metavar=options_metavar,
                add_help_option=add_help_option,
                no_args_is_help=no_args_is_help,
                hidden=hidden,
                deprecated=deprecated,
                # Rich settings
                rich_help_panel=rich_help_panel,
            )(sync_func)
            return async_func

        return decorator
