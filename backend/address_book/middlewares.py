import datetime

from django.db import connection


class SqlLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        for query in connection.queries:
            write_to_file(query.get('sql'), query.get('time'))

        return response


def write_to_file(sql_raw, execute_time):
    with open('logging/sql_logs.log', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {sql_raw}\nExecute time: {execute_time} sec\n')
