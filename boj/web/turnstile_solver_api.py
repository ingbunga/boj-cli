from typing import Optional

import requests

from boj.core import constant
from boj.core.http import JsonResponse, HttpRequest, RequestWithParams



class TurnstileSolverApiRequest(RequestWithParams):
    def __init__(
        self,
        url: str,
        sitekey: str
    ):
        self.__url = url
        self.__sitekey = sitekey

    def url(self) -> str:
        return constant.turnstile_solver_api_url(self.__url, self.__sitekey)

    def headers(self) -> Optional[dict]:
        return constant.default_headers()

    def cookies(self) -> Optional[dict]:
        return None

    def params(self) -> Optional[dict]:
        return None


class TurnstileSolverResultRequest(RequestWithParams):
    def __init__(
        self,
        req_id: str,
    ):
        self.__req_id = req_id

    def url(self) -> str:
        return constant.turnstile_solver_result_url(self.__req_id)

    def headers(self) -> Optional[dict]:
        return constant.default_headers()

    def cookies(self) -> Optional[dict]:
        return None

    def params(self) -> Optional[dict]:
        return None