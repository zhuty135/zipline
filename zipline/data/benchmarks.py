#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pandas as pd
import requests


def get_benchmark_returns(symbol):
    """
    Get a Series of benchmark returns from IEX associated with `symbol`.
    Default is `SPY`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.

    The data is provided by IEX (https://iextrading.com/), and we can
    get up to 5 years worth of data.
    """
    #jz r = requests.get(
    #jz     'https://api.iextrading.com/1.0/stock/{}/chart/5y'.format(symbol)
    #jz )
    #data = r.json()

    print('jzz','/work/jzhu/input/bmk/' + symbol + '.csv' )
    #df = pd.DataFrame(data)
    #test df = pd.read_csv('/work/jzhu/input/bmk/' + symbol + '.csv' ,index_col = 'date', parse_dates = True).sort_index()#jz r.json()
    df = pd.read_csv('/work/jzhu/input/bmk/' + symbol + '.csv' , parse_dates = True).sort_index()#jz r.json()

    df.index = pd.DatetimeIndex(df['date'])
    df = df['close']

    return df.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
