#!/usr/bin/env python3

import connexion
from swagger_server import encoder, indicepa

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple Inventory API'})
    app.run(port=8443, ssl_context='adhoc')


if __name__ == '__main__':
    main()
