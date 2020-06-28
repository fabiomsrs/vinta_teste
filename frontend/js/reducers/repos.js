export default function repos(state = [], action){
    switch (action.type){
        case 'ADD_REPO':                        
            return [...state, action.repos]
        default:
            return state;
    }
}