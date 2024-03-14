from chalice import Chalice

app = Chalice(app_name='invoke')


@app.lambda_function(name="invoke")
def invoke(event, context):
    print("Nome: ", event['nome'])
    print("Idade: ", event['idade'])
    return True