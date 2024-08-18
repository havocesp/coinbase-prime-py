# Copyright 2024-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from base_response import BaseResponse
from client import Client
from credentials import Credentials
from utils import PaginationParams, append_query_param, append_pagination_params


@dataclass
class ListPortfolioTransactionsRequest:
    portfolio_id: str
    symbols: Optional[str] = None
    types: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: List[int] = None


@dataclass
class ListPortfolioTransactionsResponse(BaseResponse):
    request: ListPortfolioTransactionsRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_portfolio_transactions(
            self,
            request: ListPortfolioTransactionsRequest) -> ListPortfolioTransactionsResponse:
        path = f"/portfolios/{request.portfolio_id}/transactions"

        query_params = append_query_param("", 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'types', request.types)

        if request.start:
            query_params = append_query_param(query_params, 'start_time', request.start.isoformat() + 'Z')
        if request.end:
            query_params = append_query_param(query_params, 'end_time', request.end.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioTransactionsResponse(response.json(), request)
