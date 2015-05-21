first: set the sys path
second: set up the celery work
The --app argument specifies the Celery app instance to use, 
it must be in the form of module.path:attribute


if u want to watch the celery running:
    use this:
    celery --app  module.path:attribute flower   or
    celery --app  module.path:attribute events
