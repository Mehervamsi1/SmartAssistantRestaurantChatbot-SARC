from Website import create_app


# This is the first code to be deployed
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)