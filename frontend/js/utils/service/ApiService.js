var urlBase = ''
if (process.env.NODE_ENV == 'production'){    
    urlBase = 'https://vinta-teste.herokuapp.com'
}
else{    
    urlBase = 'http://localhost:8000'
}

const consumeApi = (parametro = '', method = 'GET', body) => {
    return fetch(`${urlBase}/${parametro}`, {
        method,
        headers: { 'content-type': 'application/json' },
        body
    })
        .then(res => ApiService.ErrosHandling(res))
        .then(res => res.json())
}

const ApiService = {
    listRepo: (page = 1) => consumeApi('repos/?page='+page+'&user='+window.localStorage.getItem('user')),
    createRepo: (body) => consumeApi('repos/?access_token='+window.localStorage.getItem('access_token')+'&user='+window.localStorage.getItem('user'),'POST',JSON.stringify(body)),
    deleteRepo: (id) => consumeApi('repos/'+id,'DELETE'),
    listCommit: (page = 1) => consumeApi('commits/?page='+page+'&repo__user='+window.localStorage.getItem('user')),
    listRepoCommits: (repo,page = 1) => consumeApi('repos/'+repo+'/commits/?page='+page+'&repo__user='+window.localStorage.getItem('user')),
    ErrosHandling: async res => {
        if (!res.ok) {         
            await res.text().then(error => {
                throw Error(error)
            })
        }        
        return res
    }
}
export default ApiService