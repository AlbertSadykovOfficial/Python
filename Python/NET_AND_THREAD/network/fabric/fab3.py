from fabric.api import run

def iso(): 
	# run указывает fabric исп SSH, чтобы связаться с хостми, в противном случае будт использован локальный компьтер
    run('date -u')