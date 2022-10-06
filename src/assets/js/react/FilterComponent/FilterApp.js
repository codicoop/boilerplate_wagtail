import React, { useState } from 'react';
import Select from 'react-select'

export default function FilterApp(){
  console.log("backData", backData)
  const initialFormData = {
    type: "",
    model: "",
    submodel: ""
  }
  const [formData, setFormData] = useState(initialFormData)
  console.log(formData);
  const filterTitle = "Filtra els models"
  const filterTypeLabel = "Tipus"
  const filterModelLabel = "Model"
  const filterSubmodelLabel = "Submodel / Acabat"
  const filterTypeData = backData.type
  const filterModelData = backData.model
  const filterSubmodelData = backData.submodel

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
      padding: 'var(--padding-xsm) 0 var(--padding-xsm) var(--padding-lg)',
      textAlign: 'center',
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
      padding: 'var(--padding-sm)',
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
            name="type"
            placeholder={filterModelLabel}
            onChange={handleFilterChange}
          />
        </div>
        <div className="collections-detail__filters-select grid-item-10-12">
        <Select 
            styles={customStyles}
            options={filterSubmodelData} 
            name="type"
            placeholder={filterSubmodelLabel}
            onChange={handleFilterChange}
          />
        </div>
      </form>
    </section>
  )
}

