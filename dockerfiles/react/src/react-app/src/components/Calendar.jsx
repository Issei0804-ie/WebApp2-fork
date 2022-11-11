import React from 'react'

import { useState, useEffect, useContext } from "react";
import { BrowserRouter, Link, Routes, Route } from "react-router-dom";


import { getMonth } from "../util";
import { CalendarHeader } from "./CalendarHeader";
import { Month } from "./Month";
import GlobalContext from "../context/GlobalContext";
import { EventModal } from "./EventModal";



export const Calendar = () => {
    const [currentMonth, setCurrentMonth] = useState(getMonth());
    const { monthIndex, showEventModal } = useContext(GlobalContext);

    useEffect(() => {
      setCurrentMonth(getMonth(monthIndex));
    }, [monthIndex]);
  
    return (
        <>
            {showEventModal && <EventModal />}
            <div className="h-screen flex flex-col">
                <CalendarHeader />
                <div className="flex flex-1">
                
                <Month month={currentMonth} />
                </div>
            </div>
            <div>
            
                
            <Link to="/">Home</Link>
            <br />

            <Link to="/login">login</Link>


        
        </div>
        </>
    );
}
