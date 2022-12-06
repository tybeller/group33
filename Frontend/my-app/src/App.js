import React from "react";
import Header from "./Header";

function App() {
    return (
        <div className="containter">
            <Header />
        </div>
    )
}

class App extends React.Component {
    render() {
        return <h1>Hello from a class</h1>
    }
}

export default APP