import mesop as me
import wsgi_app

wsgi = wsgi_app.wsgi_app


@me.page(
  title="Mesop App Runner",
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=[
      "localhost:*",
      "https://richard-to-mesop-app-maker.hf.space",
      "https://huggingface.co",
    ]
  ),
)
def main():
  me.text("Hello World!")
