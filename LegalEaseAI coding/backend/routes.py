from fastapi import APIRouter, HTTPException

from backend.config import get_settings

from backend.schemas import (
    DocumentRequest,
    DocumentResponse
)

from backend.services.document_service import (
    DocumentService
)


router = APIRouter(
    prefix="/api",
    tags=["LegalEase"]
)


service = DocumentService(
    get_settings()
)


@router.post(
    "/generate",
    response_model=DocumentResponse
)
def generate_document(
    request: DocumentRequest
):

    try:

        return service.generate(request)

    except ValueError as exc:

        raise HTTPException(
            status_code=422,
            detail=str(exc)
        )

    except RuntimeError as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Unexpected server error: {exc}"
        )