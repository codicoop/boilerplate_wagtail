import axios from 'axios';
import React, { useEffect, useState } from 'react';
import Select from 'react-select'

import ProductCard from './ProductCard'

export default function FilterApp(){
  const initialFormData = {
    type: "",
    model: "",
    finishing: ""
  }
  const [formData, setFormData] = useState(initialFormData)
  const [imagesArray, setImagesArray] = useState([])
  const filterTitle = "Filtra els models"
  const filterTypeLabel = "Tipus"
  const filterModelLabel = "Model"
  const filterFinishingLabel = "Submodel / Acabat"
  const filterTypeData = backData.type
  const filterModelData = backData.model
  const filterFinishingData = backData.finishing
  console.log("backData", backData)
  // console.log("formData", formData);

  useEffect(()=>{
    getNewImages()
  }, [formData])
  
  const customStyles = {
    control: (provided) => ({
      ...provided,
      padding: '0',
      backgroundColor: 'transparent',
      border: '2px solid var(--blackish)',
      borderRadius: '0',
      color: 'var(--blackish)'
    }),
    option: (provided, state) => ({
      ...provided,
      borderBottom: '1px solid var(--grey-light)',
      color: 'var(--blackish)',
      backgroundColor: state.isFocused ? 'var(--grey-light)' : 'var(--white)',
      padding: 'var(--padding-xsm) var(--padding-xsm) var(--padding-xsm) var(--padding-sm)',
    }),
    menu: (provided) => ({
      ...provided,
      borderRadius: '0',
    }),
    indicatorSeparator: () => ({
      display: 'none'
    }),
    placeholder: (provided, state) => ({
      ...provided,
      color: state.isFocused ? 'var(--grey)' : 'var(--blackish)'
    })
  }
  
  return (
    <>
      <section className="collections-detail__filters">
        <form action="" className="grid-1">
          <div className="collections-detail__filters-title title-3 grid-item-1-3">
            <p>{filterTitle}</p>
          </div>
          <div className="collections-detail__filters-select grid-item-4-6">
            <Select 
              styles={customStyles}
              options={filterTypeData} 
              name="type"
              placeholder={filterTypeLabel}
              onChange={handleTypeChange}
            />
          </div>
          <div className="collections-detail__filters-select grid-item-7-9">
          <Select 
              styles={customStyles}
              options={filterModelData} 
              name="model"
              placeholder={filterModelLabel}
              onChange={handleModelChange}
            />
          </div>
          <div className="collections-detail__filters-select grid-item-10-12">
          <Select 
              styles={customStyles}
              options={filterFinishingData} 
              name="finishing"
              placeholder={filterFinishingLabel}
              onChange={handleSubmodelChange}
            />
          </div>
        </form>
      </section>
      <section className="collections-detail__product-list">
        <div className="grid-2">
          {
            imagesArray.map(printImages)
          }
        </div>
      </section>
    </>
  )

  function printImages(image) {
    return <ProductCard image={image} />
  }
  function getNewImages() {
    let parameters = []
    if (formData.finishing) {
      parameters.push(`finishing=${formData.finishing}`)
    }
    if (formData.model) {
      parameters.push(`model=${formData.model}`)
    }
    if (formData.type) {
      parameters.push(`type=${formData.type}`)
    }
    let imagesUrl = `/api/collection_items/?${parameters.join('&')}`

    axios({
      method: 'get',
      url: imagesUrl,
      headers: {'X-CSRFToken': backData.csrf}
    })
    .then(resp => {
      console.log("resposta images", resp)
      setImagesArray(resp.data)
    })
  }
  function handleTypeChange(option){
    setFormData(prevData => {
      return {
        ...prevData,
        type: option.value
      }
    })
    getNewImages()
  }
  function handleModelChange(option){
    setFormData(prevData => {
      return {
        ...prevData,
        model: option.value
      }
    })
  }
  function handleSubmodelChange(option){
    setFormData(prevData => {
      return {
        ...prevData,
        submodel: option.value
      }
    })
  }
}

