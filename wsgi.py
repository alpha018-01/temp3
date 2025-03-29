from app import app

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(debug=True)