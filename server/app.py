#!/usr/bin/env python3

from flask import Flask, request, current_app, session, g, make_response, redirect, abort

app = Flask(__name__)

@app.before_request
def print_hello ( ) :
    print( 'Hello!' )

@app.teardown_request
def print_goodbye ( something ) :
    print( 'Goodbye' )


@app.route( '/' )
def index ( ) :
    host = request.headers.get( 'Host' )
    app_name = current_app.name
    body = f"""
        <h1>This is the host: { host }</h1>
        <h2>This is the session: { session }</h2>
        <h3>This is the app's name: { app_name }</h3>
    """

    status_code = 418
    headers = {}

    response = make_response( body, status_code, headers )
    return response


@app.route( '/pop' )
def redirect_to_home ( ) :
    return redirect( '/' )

@app.route( '/abort' )
def tea_time ( ) :
    abort( 418 )


if __name__ == '__main__':
    app.run(port=5555, debug=True)
