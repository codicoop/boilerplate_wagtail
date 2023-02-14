import React from 'react';

export default function ProductCard({ image }){
  const imageUrl = image.image_thumbnail
  const modelName = translateModel(image.model)

  function openFullImage(event) {
    const thisItem = event.target
    const thisCard = thisItem.parentElement
    const thisModal = thisCard.querySelector(".modal")
    thisModal.classList.add("is-open")

    function listenerFunction(e){
        const object = thisCard.querySelector('.modal__image')
        if (!object.contains(e.target)) {
            console.log("you are clicking outside the image!");
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
            console.log("you are clicking outside the image!");
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
        // onClick={openFullImage}
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
            // onClick={closeFullImage}
          >
            <svg 
            title="{% translate 'Icon to close the image overlay' %}"
            className="icon-close icon-24" 
            viewBox="0 0 24 24" 
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M17.7556 6L6.02222 18" />
            <path d="M6.02222 6L17.7556 18" />
          </svg>
          </div>
          <div className="modal__image">
            <img src={image.image_maximized} alt={image.title} />
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
    let newModel = "Model:"
    filterModelData.map(item => {
      if (item.value == el) {
        newModel = `${newModel} ${item.label}`
      }
    })
    if (newModel === "Model:") {
      newModel = "Sense model"
    }

    return newModel
  }
}

