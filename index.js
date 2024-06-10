fetch(path.__dirname() + "/rank_generator/rank_data/ordered_list.txt")
    .then((res) => res.text())
    .then((text) => {
        console.log(text)
    })
    .catch((e) => console.error(e))