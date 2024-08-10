import './App.css'
import { TwitterFollowCard } from './TwitterFollowCard'
export function App() {

    return (
        <div className='App'>
            <TwitterFollowCard isFollowing userName="midudev" name="Miguel Angel Duran"/>
            <TwitterFollowCard isFollowing={false} userName="pheralb" name="Pablo Hernandez"/>
        </div>
    )
}