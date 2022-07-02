from flask import Flask, request
from utils.common import response_message, read_json_time_series
from utils.interpolation_methods import linear_interpolation, spline_interpolation, pad_interpolation, nearest_interpolation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def interpolation():
    req = request.get_json()
    config = req['config']
    data = read_json_time_series(req['data'], config['type'])


    if config['type'] == 'miladi':
        if config['interpolation'] == 'linear':
            result = linear_interpolation(data, config)
        elif config['interpolation'] == 'spline':
            result = spline_interpolation(data, config)
        elif config['interpolation'] == 'pad':
            result = pad_interpolation(data, config)
        elif config['interpolation'] == 'nearest':
            result = nearest_interpolation(data, config)

        result = result.to_json()
        return response_message(dict({"data": result}))
    elif config['type'] == 'shamsi':
        if config['interpolation'] == 'linear':
            result = linear_interpolation(data, config)
        elif config['interpolation'] == 'spline':
            result = spline_interpolation(data, config)
        elif config['interpolation'] == 'pad':
            result = pad_interpolation(data, config)
        elif config['interpolation'] == 'nearest':
            result = nearest_interpolation(data, config)

        result = result.to_json()
        return response_message(dict({"data": result}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
