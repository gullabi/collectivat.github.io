for f in _posts/*.markdown;do t=${f##*/}; diff $f _new_posts/${t};done;
