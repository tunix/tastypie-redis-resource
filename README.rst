-----------------------------
Redis Resource for Tastypie
-----------------------------

Allows you to create delicious APIs for Redis.

--------
Settings
--------

::

    REDIS_HOST = localhost
    REDIS_PORT = 6379
    REDIS_DATABASE = "database_name"

----------------
Example of Usage
----------------

::

    from tastypie import fields
    from tastypie.authorization import Authorization

    from tastypie_redis.resources import RedisResource, Document

    class DocumentResource(RedisResource):
        id = fields.CharField(attribute="_id")
        title = fields.CharField(attribute="title", null=True)
        entities = fields.ListField(attribute="entities", null=True)

        class Meta:
            resource_name = "documents"
            list_allowed_methods = ["delete", "get", "post"]
            authorization = Authorization()
            object_class = Document
            collection = "documents" # collection name
