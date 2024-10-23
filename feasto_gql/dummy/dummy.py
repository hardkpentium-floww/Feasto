from typing import Union

import graphene
from redis.commands.search.aggregation import Limit

from graphql_service.custom_scalars import GQLRequiredList
from feasto_core_clean_arch.models import User

class Author(graphene.ObjectType):
    id = graphene.String(required=True)
    name = graphene.String(required=True)
    email = graphene.String()
    age = graphene.Int(required=True)


class Book(graphene.ObjectType):
    id = graphene.String(required=True)
    name = graphene.String(required=True)
    author = graphene.Field(Author, required=True)
    published_on = graphene.String(required=True)


# Mutation input
class PublishBookParams(graphene.InputObjectType):
    name = graphene.String(required=True)
    author_id = graphene.String(required=True)

class GetBookParams(graphene.InputObjectType):
    id = graphene.String(required=True)
    name = graphene.String()

class AuthorNotFound(graphene.ObjectType):
    invalid_author_id = graphene.String(required=True)


class BookIsAlreadyPublished(graphene.ObjectType):
    book_name = graphene.String(required=True)

class AuthorAlreadyExists(graphene.ObjectType):
    name = graphene.String(required=True)
    message = graphene.String(required=True)

class AddAuthorParams(graphene.InputObjectType):
    name = graphene.String(required=True)
    id = graphene.String(required=True)

class AddAuthorResponse(graphene.Union):
    class Meta:
        types = (
            Author,
            AuthorAlreadyExists
        )
# Mutation response
class PublishBookResponse(graphene.Union):
    class Meta:
        types = (
            Book,
            AuthorNotFound,
            BookIsAlreadyPublished,
        )

class GetAuthorsResponse(graphene.Union):
    class Meta:
        types = (Author, AuthorNotFound)

    @classmethod
    def resolve_type(cls, instance, info):
        if isinstance(instance, Author):
            return Author
        elif isinstance(instance, AuthorNotFound):
            return AuthorNotFound
        return None


# Mutation class
class PublishBook(graphene.Mutation):
    class Arguments:
        params = PublishBookParams(required=True)

    Output = PublishBookResponse

    # Mutation trigger method
    @staticmethod
    def mutate(root, info, params) -> Union[Book, AuthorNotFound, BookIsAlreadyPublished]:
        """
        params: PublishBookParams object, this will have our mutation input data
        """
    # Write your code here which shall return any one of our result gql types

class AddAuthor(graphene.Mutation):
    class Arguments:
        params = AddAuthorParams(required=True)

    Output = AddAuthorResponse

    # Mutation trigger method
    @staticmethod
    def mutate(root, info, params) -> Union[Author, AuthorAlreadyExists]:
        isAuthorPresent = User.objects.filter(name=params.id).exists()

        if isAuthorPresent:
            return AuthorAlreadyExists(name=params.name, message="Author already exists")
        else:
            author = User.objects.create(name=params.name , id=params.id)
            author.save()
            return Author(id= str(author.id) ,name=author.name)

    # def resolve_output(self):
    #     return [Author( id= str(author.id) ,name=author.name) for author in User.objects.all()]

class AuthorBooks(graphene.ObjectType):
    books = GQLRequiredList(Book)
    total_count = graphene.Int(required=True)

class Pagination(graphene.InputObjectType):
    offset = graphene.Int(required=True)
    limit = graphene.Int(required=True)

class AuthorBooksParams(graphene.InputObjectType):
    author_id = graphene.String(required=True)
    pagination = graphene.Field(Pagination, required=True)

class AuthorBooksResponse(graphene.Union):
    class Meta:
        types = (AuthorBooks, AuthorNotFound)

class GetBookResponse(graphene.Union):
    class Meta:
        types = (Book, )

class DeleteAuthorParams(graphene.InputObjectType):
    name = graphene.String(required=True)

class DeleteAuthor(graphene.Mutation):
    class Arguments:
        params = DeleteAuthorParams(required=True)

    Output = GetAuthorsResponse  # Keep this as is

    # Mutation trigger method
    @staticmethod
    def mutate(root, info, params) -> Union[Author, AuthorNotFound]:
        author = User.objects.filter(name=params.name).first()

        if not author:
            return AuthorNotFound(invalid_author_id=params.name)  # Return AuthorNotFound if not found

        deleted_author = Author(id=str(author.id), name=author.name)  # Prepare the deleted author info
        author.delete()  # Perform the delete operation
        return deleted_author  # Return the deleted author's info
