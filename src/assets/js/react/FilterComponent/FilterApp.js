import React, { useState } from 'react';
import Select from 'react-select'

export default function FilterApp(){
  console.log("backData", backData)
  const initialFormData = {
    type: "",
    model: "",
    finishing: ""
  }
  const [formData, setFormData] = useState(initialFormData)
  console.log(formData);
  const filterTitle = "Filtra els models"
  const filterTypeLabel = "Tipus"
  const filterModelLabel = "Model"
  const filterFinishingLabel = "Submodel / Acabat"
  const filterTypeData = backData.type
  const filterModelData = backData.model
  const filterFinishingData = backData.finishing

  function handleFilterChange(option){
    setFormData(prevData => {
      return {
        ...prevData,
        [option.filter]: option.value
      }
    })
  }

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
              onChange={handleFilterChange}
            />
          </div>
          <div className="collections-detail__filters-select grid-item-7-9">
          <Select 
              styles={customStyles}
              options={filterModelData} 
              name="model"
              placeholder={filterModelLabel}
              onChange={handleFilterChange}
            />
          </div>
          <div className="collections-detail__filters-select grid-item-10-12">
          <Select 
              styles={customStyles}
              options={filterFinishingData} 
              name="finishing"
              placeholder={filterFinishingLabel}
              onChange={handleFilterChange}
            />
          </div>
        </form>
      </section>
      <section className="collections-detail__product-list">
        <div className="grid-2">
          {/* Quan tinguem el llistat de items, es mapejaran aquí */}
          {/* Així segons els filtres activats aquest llistat anirà canviant */}
        </div>
      </section>
    </>
  )
}

