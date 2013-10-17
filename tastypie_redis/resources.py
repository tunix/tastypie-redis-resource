# coding: utf-8

from bson import ObjectId

from tastypie.bundle import Bundle
from tastypie.resources import Resource


class RedisResource(Resource):
    """
    A base resource that allows to make CRUD operations for redis.
    """

    def get_object_class(self):
        return self._meta.object_class

    def get_database(self):
        """
        Developers are responsible for maintaining the connection (pool)
        and database being used.
        """
        raise NotImplementedError("You should implement get_database method.")

    def get_key(self, id=None):
        if id:
            return '%s:%s' % (self.collection, id)

        return self.collection

    def obj_get_list(self, request=None, **kwargs):
        """
        Maps redis documents to an object class.
        """
        return list(map(self.get_object_class(), self.get_database().members(self.get_key())))

    def obj_get(self, request=None, **kwargs):
        """
        Returns redis document from provided id.
        """
        return self.get_object_class()(
            self.get_database().hget(self.get_key(kwargs.get("pk")))
        )

    def obj_create(self, bundle, **kwargs):
        """
        Creates redis document from POST data.
        """
        bundle.data.update(kwargs)
        bundle.obj = self.get_database().hmset(
            self.get_key(kwargs.get("pk")),
            bundle.data
        )
        return bundle

    def obj_update(self, bundle, request=None, **kwargs):
        """
        Updates redis document.
        """
        self.get_database().update(
            {"_id": ObjectId(kwargs.get("pk"))},
            {"$set": bundle.data}
        )
        return bundle

    def obj_delete(self, request=None, **kwargs):
        """
        Removes single document from collection
        """
        parameters = {"_id": ObjectId(kwargs.get("pk"))}
        self.get_database().remove(parameters)

    def obj_delete_list(self, request=None, **kwargs):
        """
        Removes all documents from collection
        """
        self.get_database().remove()

    def detail_uri_kwargs(self, bundle_or_obj):
        """
        Given a ``Bundle`` or an object, it returns the extra kwargs needed
        to generate a detail URI.

        By default, it uses the model's ``pk`` in order to create the URI.
        """
        detail_uri_name = getattr(self._meta, 'detail_uri_name', 'pk')
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            if isinstance(bundle_or_obj.obj, ObjectId):
                kwargs[detail_uri_name] = str(bundle_or_obj.obj)
            else:
                kwargs[detail_uri_name] = getattr(bundle_or_obj.obj, detail_uri_name)
        else:
            kwargs[detail_uri_name] = getattr(bundle_or_obj, detail_uri_name)

        return kwargs
