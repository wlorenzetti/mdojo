from import_export import resources
from dojo.models import Deshi


class DeshiResource(resources.ModelResource):

    class Meta:
        model = Deshi