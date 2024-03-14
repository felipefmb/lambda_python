from chalice import Chalice

app = Chalice(app_name='scheduller')


@app.schedule("cron(5 12 ? * * *)")
def scheduled(event):
    print("Executou a função com sucesso")
    return True
