import React, { useState, useMemo, useRef ,useEffect} from 'react'
import axios from "axios";
import '../App.css';

function AboutPage () {
    return (
        <div className="AboutPage">
          <h1>The Fur-Ever Team</h1>
          <div classname="info">
            <b>Our Mission</b>
            <p>
                Our mission is to help you find your perfect pet. We want to help.
            </p><br/>
            <b>The Team</b>
            <p>
                Our team is made up of 4 people. We are all students at the
                University of Florida. We are all passionate about animals and
                want to help you find your perfect pet. We are all in the
                Computer Science program and are all in our junior year.
            </p><br/>
            <b>Members:</b>
            <p>
                <ul>
                    <li>Dante Lopez - dante.lopez@ufl.edu</li>
                    <li>Kevin Daniel - kevindaniel@ufl.edu</li>
                    <li>Eric Mercier - ej.mercier@ufl.edu</li>
                    <li>Ty Beller - tybeller@ufl.edu</li>
                </ul>
            </p>
        </div>

          


        </div>

    )

}

export default AboutPage;