import { Button } from '@mui/material'
import { useContext } from 'react';
import { UserContext } from '../contexts/user.context';
 
export default function Logout() {
 const { logOutUser } = useContext(UserContext);
 
 // This function is called when the user clicks the "Logout" button.
 const logOut = () => {
   try {
     // Calling the logOutUser function from the user context.
     const loggedOut = logOutUser();
     // Now we will refresh the page, and the user will be logged out and
     // redirected to the login page because of the <PrivateRoute /> component.
     if (loggedOut) {
       window.location.reload(true);
     }
   } catch (error) {
     alert(error)
   }
 }
 
 return (
  logOut()
  //  <>
  //    <h1>Welcome to Expengo</h1>  
  //  </>
   
 );
}