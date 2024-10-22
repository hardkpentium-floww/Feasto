import graphene
from httplib2.auth import params

from feasto_gql.dummy import PublishBook, AuthorBooksResponse, AuthorBooksParams, GetBookResponse, GetBookParams, \
    AddAuthor, GetAuthorsResponse, Author, DeleteAuthor
from graphql_service.custom_scalars import GQLRequiredList
from feasto_core_clean_arch.models import User


class Query(graphene.ObjectType):
    get_author_books = graphene.Field(
        AuthorBooksResponse,
        params=AuthorBooksParams(required=True),
        required=True,
    )

    get_books = graphene.Field(
        GetBookResponse,
        params=GetBookParams(required=True),
    )

    get_authors = graphene.List(Author, required=True)  # Update here to return a list of Author

    def resolve_get_authors(self, info):
        # Fetch all authors from your User model
        authors = User.objects.all()  # Make sure this matches your User model
        return [Author( id= str(author.id) ,name=author.name) for author in authors]



class Mutation(graphene.ObjectType):
    publish_book = PublishBook.Field(required=True)
    add_author = AddAuthor.Field(required=True)
    delete_author =DeleteAuthor.Field(required=True)

schema = graphene.Schema(query=Query, mutation=Mutation)
