import { useContext } from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";
import { UserContext } from "../contexts/user.context";
 
const PrivateRoute = () => {
 
 // Fetching the user from the user context.
 const { user } = useContext(UserContext);
 const location = useLocation();
 const redirectLoginUrl = `/login?redirectTo=${encodeURI(location.pathname)}`;
 
 // If the user is not logged in we are redirecting them
 // to the login page. Otherwise we are letting them to
 // continue to the page as per the URL using <Outlet />.
 return !user ? <Navigate to={redirectLoginUrl} /> : <Outlet /> ;
}
 
export default PrivateRoute;