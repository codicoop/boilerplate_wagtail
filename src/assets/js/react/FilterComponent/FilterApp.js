import React, { useeState, useState } from 'react';

export default function FilterApp(){
  const [filters, setFilters] = useState(initialFilters)
  const filterTitleLabel = "Filtra els models"
  const filterTypeLabel = "Tipus"
  const filterModelLabel = "Model"
  const filterSubmodelLabel = "Submodel / Acabat"
  const initialFilters = {
    type: "",
    model: "",
    submodel: ""
  }

  return(
    <section className="collections-detail__filters">
      <form action="" className="grid-1">
        <div className="collections-detail__filters-title title-3 grid-item-1-3">
          <p>{filterTitleLabel}</p>
        </div>
        <div className="collections-detail__filters-select btn btn--dark grid-item-4-6">
          <p>{filterTypeLabel}</p>
        </div>
        <div className="collections-detail__filters-select btn btn--dark grid-item-7-9">
          <p>{filterModelLabel}</p>
        </div>
        <div className="collections-detail__filters-select btn btn--dark grid-item-10-12">
          <p>{filterSubmodelLabel}</p>
        </div>
      </form>
    </section>
  )
}