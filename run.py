"""
main flask file to run
"""

from app import create_app

app = create_app()
app.run(debug=True, port=8080, host='localhost')