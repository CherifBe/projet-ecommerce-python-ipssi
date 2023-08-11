from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from infra.db import get_session
from router.auth_router import router as auth_router # TODO: update that
from router.product_router import router as product_router
from router.admin_router import router as admin_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(product_router, prefix="/product")
app.include_router(admin_router, prefix="/admin")

@app.get("/", response_class=HTMLResponse)
def hello_world():
    return """
        <html>
            <head>
                <title>Mon super site</title>
            </head>
            <body>
                <h2>Bienvenue</h2>
                <div>
                    Vous trouverez la page inscription sur la route suivante : /auth
                </div>
                <div>
                    La page connexion sur : /auth/login
                </div>
                <div>
                    La page où les produits sont listés : /product
                </div>
                <div>
                    Et enfin l'espace admin : /admin
                </div>
            </body>
        </html>
    """
    

