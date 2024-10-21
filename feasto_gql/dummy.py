from typing import Union

import graphene

from graphql_service.custom_scalars import GQLRequiredList


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


class AuthorNotFound(graphene.ObjectType):
    invalid_author_id = graphene.String(required=True)


class BookIsAlreadyPublished(graphene.ObjectType):
    book_name = graphene.String(required=True)


# Mutation response
class PublishBookResponse(graphene.Union):
    class Meta:
        types = (
            Book,
            AuthorNotFound,
            BookIsAlreadyPublished,
        )


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
