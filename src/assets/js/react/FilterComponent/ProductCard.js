import React from 'react';
import { useTranslation } from "react-i18next"

export default function ProductCard({ image }){
  const { t, i18n } = useTranslation()
  const imageUrl = image.image_thumbnail.url
  const modelName = translateModel(image.model)

  function openFullImage(event) {
    const thisItem = event.target
    const thisCard = thisItem.parentElement
    const thisModal = thisCard.querySelector(".modal")
    thisModal.classList.add("is-open")

    function listenerFunction(e){
        const object = thisCard.querySelector('.modal__image')
        if (!object.contains(e.target)) {
            thisModal.classList.remove('is-open');
        }
        window.removeEventListener("click", listenerFunction)
    }

    setTimeout(function(){
        window.addEventListener('click', listenerFunction);
    }, 100)
  }
  function closeFullImage(event) {
    const thisItem = event.target
    const thisModal = thisItem.parentElement
    const thisCard = thisModal.parentElement
    thisModal.classList.remove("is-open")

    function listenerFunction(e){
        const object = thisCard.querySelector('.modal__image')
        if (!object.contains(e.target)) {
            thisModal.classList.remove('is-open');
        }
        window.removeEventListener("click", listenerFunction)
    }

    window.removeEventListener("click", listenerFunction)
  }

  // {% image item.image width-700 as item_image %}
  return (
    <div className="product-card grid-item-4" key={image.id}>
      <div 
        className="product-card__image container-square-image" 
        style={
          {"backgroundImage": `url(${imageUrl})`}
        }
        onClick={openFullImage}
      ></div>
      <div className="product-card__label">
        <div className="product-card__title">
          <p>{image.title}</p>
        </div>
        <div className="product-card__text">
          <p>{modelName}</p>
        </div>
        <div className="product-card__text">
          {
            image.finishings.map(item => {
              return <p key={item.id}>{item.title}</p>
            })
          }
        </div>
      </div>
      <div className="modal">
        <div className="modal__container">
          <div 
            className="modal__icon" 
            onClick={closeFullImage}
          >
            <svg 
            className="icon-close icon-24" 
            viewBox="0 0 24 24" 
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M17.7556 6L6.02222 18" />
            <path d="M6.02222 6L17.7556 18" />
          </svg>
          </div>
          <div className="modal__image">
            <img src={image.image_maximized.url} alt={image.image_maximized.alt} />
          </div>
        </div>
        <div className="modal__title title-3">
          <p>{image.title}</p>
        </div>
      </div>
    </div>
  )

  function translateModel(el) {
    const filterModelData = backData.model
    let newModel = ""
    filterModelData.map(item => {
      if (item.value == el) {
        newModel = `${t('Model:')} ${newModel} ${item.label}`
      }
    })
    if (newModel === "") {
      newModel = t('Without_model')
    }

    return newModel
  }
}

