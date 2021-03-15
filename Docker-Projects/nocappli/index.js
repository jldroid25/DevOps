const express = require('express')
const app = express()
const port = 3000
// Building a User A.PI
app.get('/', (req, res) => {

  res.json([
      { 
      name:     'Jldroid25',
      email:    'jldroid25@hackermail.hack',
      position: 'Site Reliability Engineer'
     },
     { 
        name:     'MindHunter',
        email:    'Mhunter@devops.sre',
        position: 'Devops Engineer'
       },

       { 
        name:     'RubiconP',
        email:    'rubic@puttyfun.facks',
        position: 'Network Operation Center'
       },

       { 
        name:     'DevCoder',
        email:    'fbdevsupport@fb.com.uk',
        position: 'Developer Support Engineer'
       }

    ])
    
    })

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})