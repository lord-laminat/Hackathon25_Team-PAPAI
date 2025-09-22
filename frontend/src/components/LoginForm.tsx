import { useState } from 'react'
import styles from '../styles/LoginForm.module.css';

console.log(styles);

export default function LoginForm() {
  const [count, setCount] = useState(0)

  return (
    <div className="login-container">
        <h1># login</h1>
        
        <form>
            <div className={styles["form-group"]}>
                <label htmlFor="username">Username</label>
                <input type="text" id="username" name="username" required></input>
            </div>
            
            <div className={styles["form-group"]}>
                <label htmlFor="password">Password</label>
                <input type="password" id="password" name="password" required></input>
            </div>
            
            <div className={styles["checkbox-group"]}>
                <input type="checkbox" id="remember" name="remember"></input>
                <label htmlFor="remember">Remember me</label>
            </div>
            
            <div className={styles["form-group"]}>
                <label htmlFor="target-password">Target Password?</label>
                <input type="password" id="target-password" name="target-password"></input>
            </div>
            
            <button type="submit">Login</button>
        </form>
    </div>
  )
}
