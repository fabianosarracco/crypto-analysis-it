import datetime

def daterange(start_date, end_date, step = 1):
    '''
        Generatore di tutte le date comprese in un intervallo specificato.
    '''
    for n in range(0, int ((end_date - start_date).days) + 1, step):
        yield start_date + datetime.timedelta(n)