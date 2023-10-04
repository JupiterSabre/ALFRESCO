from Website import create_app

app = create_app()


if __name__ == "__main__":
    print("app initialized 👍🏽")
    app.run(debug=True)