// 查找缺失的文件

const fs = require('fs');

fs.readdir('./images', (err, folders) => {
    folders.forEach(folder => {
        fs.readdir(`./images/${folder}/`, (err, files) => {
            for (let i = 0; i < files.length; i++) {
                if (!files.includes(`${i}_${folder}.jpg`)) {
                    console.log(`${folder}/${i}_${folder}.jpg`);
                }
            }
        });
    });
});
