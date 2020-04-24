function hiddenness = find_neuron_alpha_shapes(fname, neuron_name)
% Find the first alpha-shape value which includes all neural points for a
% variety of different alpha values. This functions constructs many
% different alpha shapes with different alpha values, and then check
% whether each collision is located inside that newly-generated alpha
% shape.
    neuron = read_neuron_data(fname);
    shape = alphaShape(neuron);
    alphas = get_alpha_values_to_process(shape);
    table_size = [size(neuron, 1), size(alphas, 1)];
    collisions_with_all_alphas = create_collision_table(alphas, table_size);
    is_hidden = uint8(zeros(length(neuron), 1));
    % We iterate over VariableNames and not directly over the alpha values
    % since a bug caused the final table to have more than the pre-set
    % number of columns in it.
    alpha_str = collisions_with_all_alphas.Properties.VariableNames;
    for alpha_num = 1:length(alphas)
        shape.Alpha = alphas(alpha_num);
        rows_of_hidden_colls = find_hidden_collisions(shape, neuron);
        is_hidden(rows_of_hidden_colls) = uint8(1);
        collisions_with_all_alphas.(alpha_str{alpha_num}) = is_hidden;
        is_hidden(:) = uint8(0);
    end
    hiddenness = sum(collisions_with_all_alphas.Variables, 2);
    save_results(hiddenness, neuron_name);
end