import qs from 'qs';

export default {
    post(that, url, postdata, success) {
        that.$axios.post(url, qs.stringify(postdata))
            .then(success)
            .catch(err => {
                console.log(err);
                // that.$Modal.error({
                //     title: '错误提示',
                //     content: '很抱歉，网络请求失败，请稍后再试',
                // });
            });

    },
    get(that, url, success) {
        that.$axios.get(url, {headers: {'Authorization': localStorage.getItem('Authorization')}})
            .then(success)
            .catch(err => {
                console.log(err);
                // that.$Modal.error({
                //     title: '错误提示',
                //     content: '很抱歉，网络请求失败，请稍后再试',
                // });
            });

    }
}