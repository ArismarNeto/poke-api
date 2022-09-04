from app import create_app
print(__name__)
app = create_app()

app.run(debug=True)
