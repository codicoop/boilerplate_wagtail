import React from 'react';

export default function ProductCard(){
  // {% image item.image width-700 as item_image %}
  return (
    // <div className="product-card grid-item-4">
    //   <div 
    //     className="product-card__image container-square-image" 
    //     style={`--bg-image: url(${imageUrl})`}
    //     onClick="openFullImage(event)"
    //   ></div>
    //   <div className="product-card__label">
    //     <div className="product-card__title">
    //       <p>{{ item.model }}</p>
    //     </div>
    //     <div className="product-card__text">
    //       {% for finishing in item.finishings.all %}
    //       <p>{{ finishing }}</p>
    //       {% endfor %}
    //     </div>
    //     <div className="product-card__text">
    //       {% for item_type in item.types.all %}
    //       <p>Item type: {{ item_type }}</p>
    //       {% endfor %}
    //     </div>
    //   </div>
    //   <div className="modal">
    //     <div className="modal__container">
    //       <div className="modal__icon" onclick="closeFullImage(event)">
    //         <svg 
    //         title="{% translate 'Icon to close the image overlay' %}"
    //         className="icon-close icon-24" 
    //         viewbox="0 0 24 24" 
    //         xmlns="http://www.w3.org/2000/svg"
    //       >
    //         <path d="M17.7556 6L6.02222 18" />
    //         <path d="M6.02222 6L17.7556 18" />
    //       </svg>
    //       </div>
    //       <div className="modal__image">
    //         {% image item.image original %}
    //       </div>
    //     </div>
    //     <div className="modal__title title-3">
    //       <p>{{ item.model }}</p>
    //     </div>
    //   </div>
    // </div>
  )
}

