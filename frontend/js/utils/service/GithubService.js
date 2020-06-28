const urlBase = 'https://api.github.com'

const consumeApi = (parameter = '', method = 'GET', body) => {    
    const access_token = window.localStorage.getItem("access_token")
    const headers = {'content-type': 'application/json'}
    if(access_token){
        headers['Authorization'] = 'token ' + access_token
    }    
    return fetch(`${urlBase}/${parameter}`, {
        method,
        headers,
        body
    })
        .then(res => GithubService.ErrosHandling(res))
        .then(res => res.json())
}

const GithubService = {
    getUser: () => consumeApi('user'),
    listRepo: (user) => consumeApi('repos/'+user),    
    getRepo: (user, repo) => consumeApi('repos/'+user+'/'+repo),
    listCommit: (user,repo) => consumeApi('repos/'+user+'/' + repo +'/commits'),
    ErrosHandling: res => {
        if (!res.ok) {            
            throw Error(res)
        }
        return res
    }
}
export default GithubService