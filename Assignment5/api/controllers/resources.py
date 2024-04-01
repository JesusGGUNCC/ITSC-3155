from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, resources):
    db_resources = models.Resource(
        item=resources.item,
        amount=resources.amount
    )

    db.add(db_resources)

    db.commit()

    db.refresh(db_resources)

    return db_resources


def read_all(db: Session):
    return db.query(models.Resource).all()


def read_one(db: Session, resource_id):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()


def update(db: Session, resource_id, resources):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)

    update_data = resources.model_dump(exclude_unset=True)

    db_resource.update(update_data, synchronize_session=False)

    db.commit()

    return db_resource.first()


def delete(db: Session, resource_id):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)

    db_resource.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
